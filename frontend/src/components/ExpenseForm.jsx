import { useState } from "react";
import API from "../services/api";

function ExpenseForm({ refresh }) {

const [expense,setExpense]=useState({

title:"",
amount:"",
category:"",
description:""

});

const handleChange=(e)=>{

setExpense({

...expense,

[e.target.name]:e.target.value

});

};

const submit=async(e)=>{

e.preventDefault();

await API.post("/expenses/add",expense);

setExpense({

title:"",
amount:"",
category:"",
description:""

});

refresh();

};

return(

<form
onSubmit={submit}
className="bg-white shadow rounded p-6 mb-8 space-y-4"
>

<input
name="title"
placeholder="Title"
value={expense.title}
onChange={handleChange}
className="border p-3 rounded w-full"
/>

<input
name="amount"
type="number"
placeholder="Amount"
value={expense.amount}
onChange={handleChange}
className="border p-3 rounded w-full"
/>

<select
name="category"
value={expense.category}
onChange={handleChange}
className="border p-3 rounded w-full"
>

<option value="">Category</option>

<option>Payroll</option>

<option>Cloud Infrastructure</option>

<option>AI Infrastructure</option>

<option>Software</option>

<option>Marketing</option>

<option>Office</option>

<option>Hardware</option>

<option>Travel</option>

<option>Legal</option>

<option>Misc</option>

</select>

<input
name="description"
placeholder="Description"
value={expense.description}
onChange={handleChange}
className="border p-3 rounded w-full"
/>

<button
className="bg-blue-600 text-white px-6 py-3 rounded"
>

Add Expense

</button>

</form>

);

}

export default ExpenseForm;