import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function ExpenseChart({ expenses }) {

  const daily = {};

  expenses.forEach((e) => {
    daily[e.date] = (daily[e.date] || 0) + Number(e.amount);
  });

  const data = Object.entries(daily)
    .sort((a, b) => new Date(a[0]) - new Date(b[0]))
    .map(([date, amount]) => ({
      date,
      amount
    }));

  return (
    <div className="bg-white rounded shadow p-6 mt-8">
      <h2 className="text-2xl font-bold mb-5">
        Expense Trend
      </h2>

      <ResponsiveContainer width="100%" height={350}>
        <LineChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />

          <XAxis dataKey="date" hide />

          <YAxis />

          <Tooltip />

          <Line
            type="monotone"
            dataKey="amount"
            stroke="#2563EB"
            strokeWidth={3}
          />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default ExpenseChart;