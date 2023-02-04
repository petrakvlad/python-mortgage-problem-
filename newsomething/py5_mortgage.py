import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# calc monthly payment
def find_payment(loan, rate, months):
    return loan*((rate*(1+rate)**months)/((1+rate)**months - 1))

# compare morts
def compare_morts(amt, years, fixed_rate, pts, pts_rate, var_rate1, var_rate2, var_months):
    totmonth = years*12
    fixed1 = Fixed(amt, fixed_rate, totmonth)
    fixed2 = Fixed_with_pts(amt, pts_rate, totmonth, pts)
    two_rate = Two_rates(amt, var_rate2, totmonth, var_rate1, var_months)
    morts = [fixed1, fixed2, two_rate]
    for i in range(totmonth):
        for each in morts:
            each.make_payment()
    plot_morts(morts)


#make a graph of mortgages
def plot_morts(morts):
    def label_plot(figure, title, xlabel, ylable):
        plt.figure(figure)
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylable)
        plt.legend(loc = "best")
    
    styles = ['k-', 'k-.', 'k:']

    payments, cost, balance, netcost = 0,1,2,3

    for i in range(len(morts)):
        plt.figure(payments)
        morts[i].plot_payment(styles[i])
        plt.figure(cost)
        morts[i].plot_tot_paid(styles[i])
        plt.figure(balance)
        morts[i].plot_outstanding(styles[i])
        plt.figure(netcost)
        morts[i].plot_net(styles[i])

    label_plot(payments, "Monthly payment", "Monthes", "Cash")
    label_plot(cost, "Compound paid", "Monthes", "Cash")
    label_plot(balance, "Body of credit", "Monthes", "Cash")
    label_plot(netcost, "Net cost of credit", "Monthes", "Cash")



#base class of mortagge
class Mortgage(object):
    def __init__(self, loan, ann_rate, months):
        self._legend = None
        self._loan = loan
        self._rate = ann_rate/12
        self._months = months
        self._paid = [0.0]
        self._outstanding = [loan]
        self._payment = find_payment(self._loan, self._rate, self._months)


    def make_payment(self):
        self._paid.append(self._payment)
        reduction = self._payment - self._outstanding[-1]*self._rate
        self._outstanding.append(self._outstanding[-1] - reduction)

        
    def get_total_paid(self):
        return sum(self._paid)
    
    def __str__(self):
        return self._legend
    

    # plotting methods
    def plot_payment(self, style):
        plt.plot(self._paid[1:], label = self._legend)

    def plot_outstanding(self, style):
        plt.plot(self._outstanding[1:], style, label = self._legend)

    def plot_tot_paid(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])
        plt.plot(tot_pd, style, label = self._legend)

    def plot_net(self, style):
        tot_pd = [self._paid[0]]
        for i in range(1, len(self._paid)):
            tot_pd.append(tot_pd[-1] + self._paid[i])

        equity_paid = np.array([self._loan]*len(self._outstanding))
        equity_paid = equity_paid - np.array(self._outstanding)

        net = np.array(tot_pd) - equity_paid

        plt.plot(net, style, label = self._legend)



    
    
    
# Different types of mortgages

class Fixed(Mortgage):
    def __init__(self, loan, ann_rate, months):
        super().__init__(loan, ann_rate, months)
        self._legend = f"Fixed, {ann_rate*100:.1f}%"



class Fixed_with_pts(Mortgage):
    def __init__(self, loan, ann_rate, months, pts):
        super().__init__(loan, ann_rate, months)
        self._pts = pts
        self._paid = [loan*(pts/100)]
        self._legend = f"Fixed, {ann_rate*100:.1f}%, {pts} points"


class Two_rates(Mortgage):
    def __init__(self, loan, ann_rate, months, teaser_rate, teaser_month):
        super().__init__(loan, teaser_rate, months)
        self._teaser_rate = teaser_rate
        self._teaser_month = teaser_month
        self._nextRate = ann_rate/12
        self._legend = (f"{teaser_rate*100:.1f}% for " +
            f"{self._teaser_month} months, then {100*ann_rate:.1f}%")


    def make_payment(self):
        if len(self._paid) == self._teaser_month + 1:
            self._rate = self._nextRate
            self._payment = find_payment(self._outstanding[-1], self._rate, self._months - self._teaser_month)

        Mortgage.make_payment(self)



compare_morts(amt=200000, years=30, fixed_rate=0.07,
pts = 3.25, pts_rate=0.05, var_rate1=0.045,
var_rate2=0.095, var_months=48)
plt.show()


