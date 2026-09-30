import matplotlib.pyplot as plt
months=["Jan","Feb","Mar","APr","May","Jun"]
sales=[120,140,160,220,180,250]
expenses=[70,90,110,100,130,150]
fig,ax=plt.subplots(2,1,figsize=(10,8))
ax[0].plot(
    months,
    sales,
    marker="o",
    linewidth=2,
    label="Sales"
)
ax[0].set_title("Monthly Sales")
ax[0].set_xlabel("Month")
ax[0].set_ylabel("Sales")
ax[0].set_xticks(range(len(months)))
ax[0].set_xticklabels(months)
ax[0].annotate(
    "Highest Sales",
    xy=(5,250),
    xytext=(3.5,270),
    arrowprops=dict(arrowstyle="->")
)
ax[0].legend()
ax[0].grid(True)
#expenses
ax[1].plot(
    months,
    expenses,
    marker="s",
    linewidth=2,
    label="Expenses"
)
ax[1].set_xticks(range(len(months)))
ax[1].set_xticklabels(months)
ax[1].set_xticklabels(months)
ax[1].set_xticklabels(months)
ax[1].annotate(
    "Highest Expense",
    xy=(5,160),
    xytext=(3.5,180),
    arrowprops=dict(arrowstyle="->")
)
ax[1].legend()
ax[1].grid(True)
fig.suptitle("Monthly Sales and Expenses Analysis",fontsize=16)
plt.tight_layout()
plt.savefig(
    "monthly_sales_expenses.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()