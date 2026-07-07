import { useEffect, useState } from "react";
import API from "../services/api";

function AIInsights() {
  const [data, setData] = useState(null);

  useEffect(() => {
    API.get("/analytics/anomalies")
      .then((res) => {
        console.log(res.data); // Check what backend sends
        setData(res.data);
      })
      .catch((err) => {
        console.error(err);
      });
  }, []);

  if (!data) {
    return (
      <div className="bg-white rounded shadow p-6 mt-8">
        Loading AI Insights...
      </div>
    );
  }

  const anomalies = data.anomalies || [];

  return (
    <div className="bg-white rounded shadow p-6 mt-8">
      <h2 className="text-2xl font-bold mb-6">
        🤖 AI Insights
      </h2>

      {anomalies.length === 0 ? (
        <p>No anomalies found.</p>
      ) : (
        anomalies.map((item, index) => (
          <div
            key={index}
            className="border-l-4 border-red-500 bg-red-50 p-4 mb-4 rounded"
          >
            <h3 className="font-bold">{item.title}</h3>

            <p><strong>Category:</strong> {item.category}</p>

            <p><strong>Amount:</strong> ₹ {item.amount}</p>

            <p><strong>Risk:</strong> {item.risk}</p>

            <p><strong>Reason:</strong> {item.reason}</p>

            <p className="text-blue-600">
              {item.recommendation}
            </p>
          </div>
        ))
      )}
    </div>
  );
}

export default AIInsights;