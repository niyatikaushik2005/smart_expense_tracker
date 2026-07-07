import {
  PieChart,
  Pie,
  Tooltip,
  Cell,
  ResponsiveContainer
} from "recharts";

const COLORS = [
  "#2563EB",
  "#10B981",
  "#F59E0B",
  "#EF4444",
  "#8B5CF6",
  "#EC4899",
  "#14B8A6",
  "#6366F1"
];

function CategoryPie({ expenses }) {

  const grouped = {};

  expenses.forEach((e) => {
    grouped[e.category] = (grouped[e.category] || 0) + Number(e.amount);
  });

  const data = Object.entries(grouped).map(([name, value]) => ({
    name,
    value
  }));

  return (
    <div className="bg-white rounded shadow p-6 mt-8">
      <h2 className="text-2xl font-bold mb-5">
        Category Distribution
      </h2>

      <ResponsiveContainer width="100%" height={350}>
        <PieChart>

          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={120}
            label
          >

            {data.map((entry, index) => (
              <Cell
                key={index}
                fill={COLORS[index % COLORS.length]}
              />
            ))}

          </Pie>

          <Tooltip />

        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}

export default CategoryPie;