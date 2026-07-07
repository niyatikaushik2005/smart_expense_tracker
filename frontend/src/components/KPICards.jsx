function KPICards({ expenses }) {

    const total = expenses.reduce((sum,e)=>sum+e.amount,0);

    const monthly = expenses
    .filter(e=>new Date(e.date).getMonth()===new Date().getMonth())
    .reduce((sum,e)=>sum+e.amount,0);

    return(

<div className="grid grid-cols-3 gap-6 my-6">

<div className="bg-white shadow rounded p-5">

<h3 className="text-gray-500">

Total Expense

</h3>

<p className="text-3xl font-bold">

₹ {total.toLocaleString()}

</p>

</div>

<div className="bg-white shadow rounded p-5">

<h3 className="text-gray-500">

Monthly Expense

</h3>

<p className="text-3xl font-bold">

₹ {monthly.toLocaleString()}

</p>

</div>

<div className="bg-white shadow rounded p-5">

<h3 className="text-gray-500">

Transactions

</h3>

<p className="text-3xl font-bold">

{expenses.length}

</p>

</div>

</div>

    );

}

export default KPICards;