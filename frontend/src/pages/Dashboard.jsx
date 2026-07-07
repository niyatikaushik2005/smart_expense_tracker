import { useEffect, useState } from "react";
import API from "../services/api";

import Navbar from "../components/Navbar";
import KPICards from "../components/KPICards";
import ExpenseForm from "../components/ExpenseForm";
import ExpenseTable from "../components/ExpenseTable";
import ExpenseChart from "../components/ExpenseChart";
import CategoryPie from "../components/CategoryPie";
import ForecastChart from "../components/ForecastChart";
import AIInsights from "../components/AIInsights";

function Dashboard() {
  const [expenses, setExpenses] = useState([]);

  const loadExpenses = async () => {
    try {
      const res = await API.get("/expenses");
      setExpenses(res.data);
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    loadExpenses();
  }, []);

  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />

      <div className="max-w-7xl mx-auto p-8">
        <KPICards expenses={expenses} />

        <ExpenseForm refresh={loadExpenses} />

        <ExpenseTable
          expenses={expenses}
          refresh={loadExpenses}
        />

        <ExpenseChart expenses={expenses} />

        <CategoryPie expenses={expenses} />

        <ForecastChart />

        <AIInsights />
      </div>
    </div>
  );
}

export default Dashboard;