import API from "../services/api";

function ExpenseTable({ expenses, refresh }) {

const remove=async(id)=>{

await API.delete(`/expenses/${id}`);

refresh();

};

return(

<div className="bg-white rounded shadow p-6">

<h2 className="text-2xl font-bold mb-5">

Recent Expenses

</h2>

<table className="w-full">

<thead>

<tr className="border-b">

<th>Title</th>

<th>Category</th>

<th>Amount</th>

<th>Date</th>

<th></th>

</tr>

</thead>

<tbody>

{

expenses.map((e)=>(

<tr key={e._id} className="border-b">

<td>{e.title}</td>

<td>{e.category}</td>

<td>₹ {e.amount}</td>

<td>{e.date}</td>

<td>

<button

onClick={()=>remove(e._id)}

className="text-red-600"

>

Delete

</button>

</td>

</tr>

))

}

</tbody>

</table>

</div>

);

}

export default ExpenseTable;