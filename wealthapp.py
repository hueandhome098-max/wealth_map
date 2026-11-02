import streamlit as st

# Page Setup & Brandings
st.set_page_config(page_title="WealthMap", page_icon="💰", layout="wide")

st.title("WealthMap: Your Personal Financial Navigator")
st.subheader("Know your money. Control your future.")
st.markdown("---")

# =========================================================
# GLOBAL INPUT HUB (Single Place for All User Inputs)
# =========================================================
st.sidebar.header("🎛️ Financial Profile Inputs")
st.sidebar.markdown("Enter your values once. All modules update automatically!")

monthly_income = st.sidebar.number_input("Monthly Income (₹)", min_value=0, value=65000, step=1000)
monthly_expenses = st.sidebar.number_input("Monthly Expenses (₹)", min_value=0, value=38000, step=1000)
cash_in_hand = st.sidebar.number_input("Cash in Hand (₹)", min_value=0, value=8500, step=500)
bank_balance = st.sidebar.number_input("Bank Balance (₹)", min_value=0, value=120000, step=5000)
investments = st.sidebar.number_input("Total Investments (₹)", min_value=0, value=75000, step=5000)
loans_debts = st.sidebar.number_input("Total Loans / Debts (₹)", min_value=0, value=35000, step=5000)

st.sidebar.markdown("---")
st.sidebar.header("⚠️ Impulse / Overspending Log")
overspent_amount = st.sidebar.number_input("Overspent This Month (₹)", min_value=0, value=0, step=500,
                                           help="Unexpected expenses or impulsive shopping.")

# =========================================================
# CORE CALCULATIONS ENGINE
# =========================================================
liquid_assets = cash_in_hand + bank_balance
total_assets = liquid_assets + investments
net_worth = total_assets - loans_debts

# Baseline Savings & Adjusted Savings (After Overspending)
base_savings = monthly_income - monthly_expenses
net_savings = base_savings - overspent_amount

# Savings Rates
savings_rate = (net_savings / monthly_income * 100) if monthly_income > 0 else 0

# Emergency Survival Coverage (Months)
if monthly_expenses > 0:
    emergency_months = liquid_assets / monthly_expenses
else:
    emergency_months = 999.0

# ---------------------------------------------------------
# DYNAMIC FINANCIAL HEALTH SCORE (Includes Overspending)
# ---------------------------------------------------------
health_score = 0

# 1. Emergency Safety Score (Max 30 pts)
if emergency_months >= 6:
    health_score += 30
elif emergency_months >= 3:
    health_score += 20
else:
    health_score += 10

# 2. Savings Discipline Score (Max 30 pts)
if savings_rate >= 20:
    health_score += 30
elif savings_rate >= 10:
    health_score += 20
elif savings_rate > 0:
    health_score += 10
else:
    health_score += 0  # Penalty for zero/negative savings

# 3. Debt Control Score (Max 25 pts)
if loans_debts == 0:
    health_score += 25
elif loans_debts < (total_assets * 0.5):
    health_score += 15
else:
    health_score += 5

# 4. Overspending Habit Score (Max 15 pts)
if overspent_amount == 0:
    health_score += 15
elif overspent_amount <= (monthly_income * 0.10):
    health_score += 8
else:
    health_score += 0  # 0 points for heavy overspending

# =========================================================
# 7-MODULE MULTI-TAB NAVIGATION
# =========================================================
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Overview",
    "💎 Net Worth & Liquidity",
    "🛡️ Emergency Coverage",
    "📊 Savings & Budget",
    "⚠️ Overspending Impact",
    "🏆 Health Scorecard",
    "💡 Expert Roadmap"
])

# ---------------------------------------------------------
# TAB 1: OVERVIEW & DASHBOARD
# ---------------------------------------------------------
with tab1:
    st.header("Welcome to WealthMap Dashboard")
    st.success("### “Do not save what is left after spending, but spend what is left after saving.” – *Warren Buffett*")

    st.markdown("Your financial command center. All metrics are calculated live from your sidebar inputs.")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Net Worth", f"₹{net_worth:,.2f}")
    c2.metric("Liquid Assets", f"₹{liquid_assets:,.2f}")
    c3.metric("Net Savings Rate", f"{savings_rate:.1f}%")
    c4.metric("Emergency Survival", f"{emergency_months:.1f} Months")

# ---------------------------------------------------------
# TAB 2: NET WORTH & LIQUIDITY
# ---------------------------------------------------------
with tab2:
    st.header("💎 Net Worth & Liquidity Breakdown")
    col_a, col_b = st.columns(2)

    with col_a:
        st.info("### Assets")
        st.write(f"- Cash in Hand: **₹{cash_in_hand:,.2f}**")
        st.write(f"- Bank Balance: **₹{bank_balance:,.2f}**")
        st.write(f"- Investments: **₹{investments:,.2f}**")
        st.markdown(f"**Total Assets:** `₹{total_assets:,.2f}`")

    with col_b:
        st.error("### Liabilities")
        st.write(f"- Active Loans / Debts: **₹{loans_debts:,.2f}**")
        st.markdown(f"**Total Liabilities:** `₹{loans_debts:,.2f}`")

    st.markdown("---")
    st.subheader(f"Your True Net Worth: ₹{net_worth:,.2f}")
    st.metric("Quick-Access Cash (Liquidity)", f"₹{liquid_assets:,.2f}")

# ---------------------------------------------------------
# TAB 3: EMERGENCY COVERAGE ENGINE
# ---------------------------------------------------------
with tab3:
    st.header("🛡️ Emergency Coverage Engine")
    st.metric("Emergency Survival Duration", f"{emergency_months:.1f} Months")

    if emergency_months < 3:
        st.error(
            "🚨 **High Risk:** Your liquid cash covers less than 3 months of expenses. Focus on building an emergency reserve.")
    elif emergency_months < 6:
        st.warning("⚠️ **Moderate Safety:** You have a fair buffer, but aim for a full 6-month safety net.")
    else:
        st.success("🏆 **Secure Buffer:** Outstanding! You possess a robust 6+ month emergency cushion.")

# ---------------------------------------------------------
# TAB 4: SAVINGS RATE & BUDGET ALLOCATOR
# ---------------------------------------------------------
with tab4:
    st.header("📊 Savings & 50-30-20 Budget Allocator")
    col_s1, col_s2 = st.columns(2)

    with col_s1:
        st.metric("Net Savings After Expenses & Overspending", f"₹{net_savings:,.2f}")
        st.metric("Effective Savings Rate", f"{savings_rate:.1f}%")

    with col_s2:
        st.info("### 50-30-20 Budget Blueprint")
        st.write(f"- **Needs (50%):** ₹{(monthly_income * 0.50):,.2f}")
        st.write(f"- **Wants (30%):** ₹{(monthly_income * 0.30):,.2f}")
        st.write(f"- **Target Savings (20%):** ₹{(monthly_income * 0.20):,.2f}")

# ---------------------------------------------------------
# TAB 5: OVERSPENDING IMPACT TRACKER
# ---------------------------------------------------------
with tab5:
    st.header("⚠️ Overspending Impact Tracker")
    st.markdown("See how your impulsive purchases directly impact your financial safety.")

    o1, o2, o3 = st.columns(3)
    o1.metric("Original Monthly Savings", f"₹{base_savings:,.2f}")
    o2.metric("Amount Overspent", f"₹{overspent_amount:,.2f}")
    o3.metric("Final Net Savings", f"₹{net_savings:,.2f}", delta=f"-₹{overspent_amount}")

    st.markdown("---")
    if overspent_amount == 0:
        st.success(
            "🎉 **Clean Discipline!** You have 0 overspending logged this month. You earned full bonus points on your Health Scorecard!")
    elif net_savings < 0:
        st.error(
            f"🚨 **Deficit Alert:** You overspent by ₹{overspent_amount:,.2f}, putting your monthly budget in the RED. You are consuming your existing savings!")
    else:
        st.warning(
            f"⚠️ **Savings Drained:** Overspending reduced your total monthly savings to ₹{net_savings:,.2f}. Try to minimize non-essential purchases.")

# ---------------------------------------------------------
# TAB 6: HEALTH SCORECARD & GAMIFICATION
# ---------------------------------------------------------
with tab6:
    st.header("🏆 Financial Health Scorecard")
    st.markdown("Dynamic score calculated from Emergency Safety, Savings Rate, Debt Control, and Overspending Habits.")

    st.subheader(f"Overall Score: {health_score} / 100")
    st.progress(health_score / 100)

    if health_score >= 80:
        st.success("🏆 **Tier: Wealth Master** — Outstanding financial discipline across all metrics!")
    elif health_score >= 60:
        st.info("🚀 **Tier: Financial Explorer** — Solid base, but cut down impulse spending or clear debt.")
    elif health_score >= 40:
        st.warning(
            "⚠️ **Tier: Money Learner** — Caution advised. Overspending or low liquidity is hurting your progress.")
    else:
        st.error("🚨 **Tier: Risk Zone** — Vulnerable financial state. Immediate budget control required.")

# ---------------------------------------------------------
# TAB 7: EXPERT ROADMAP & RECOMMENDATIONS
# ---------------------------------------------------------
with tab7:
    st.header("💡 Expert Financial Roadmap")

    if overspent_amount > 0:
        st.error(
            f"• **Overspending Control:** You overspent ₹{overspent_amount:,.2f} this month. Audit discretionary expenses to protect your savings rate.")
    else:
        st.success("• **Overspending Control:** Excellent impulse control!")

    if emergency_months < 3:
        st.warning("• **Emergency Reserve:** Build your liquid bank balance until it covers 3–6 months of expenses.")
    else:
        st.success("• **Emergency Reserve:** Solid safety net maintained!")

    if loans_debts > 0:
        st.warning("• **Debt Strategy:** Pay off active liabilities to strengthen your Net Worth.")
    else:
        st.success("• **Debt Strategy:** Completely debt-free!")
