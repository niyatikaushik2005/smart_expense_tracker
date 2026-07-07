import { useEffect, useState } from "react";
import API from "../services/api";

import {
  LineChart,
  Line,
  Tooltip,
  XAxis,
  YAxis,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function ForecastChart() {

  const [forecast, setForecast] = useState([]);

  useEffect(() => {

    API.get("/analytics/forecast")
      .then((res) => {

        setForecast(res.data.forecast);

      });

  }, []);

  return (

<div className="bg-white rounded shadow p-6 mt-8">

<h2 className="text-2xl font-bold mb-5">

30-Day Forecast

</h2>

<ResponsiveContainer width="100%" height={350}>

<LineChart data={forecast}>

<CartesianGrid strokeDasharray="3 3"/>

<XAxis dataKey="date" hide/>

<YAxis/>

<Tooltip/>

<Line

dataKey="predicted_expense"

stroke="#10B981"

strokeWidth={3}

/>

</LineChart>

</ResponsiveContainer>

</div>

);

}

export default ForecastChart;