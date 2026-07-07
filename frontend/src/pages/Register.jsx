import { useState } from "react";
import { Link,useNavigate } from "react-router-dom";
import API from "../services/api";

function Register(){

const navigate=useNavigate();

const [form,setForm]=useState({

name:"",
email:"",
password:""

});

const handleChange=(e)=>{

setForm({

...form,

[e.target.name]:e.target.value

});

};

const handleSubmit=async(e)=>{

e.preventDefault();

try{

await API.post("/auth/register",form);

alert("Registration Successful");

navigate("/");

}

catch(err){

alert(err.response?.data?.detail);

}

};

return(

<div className="min-h-screen flex justify-center items-center">

<div className="bg-white p-8 rounded-xl shadow-xl w-[420px]">

<h1 className="text-3xl font-bold text-center mb-6">

Create Account

</h1>

<form

onSubmit={handleSubmit}

className="space-y-4"

>

<input

name="name"

placeholder="Name"

className="border p-3 rounded w-full"

onChange={handleChange}

/>

<input

name="email"

placeholder="Email"

className="border p-3 rounded w-full"

onChange={handleChange}

/>

<input

type="password"

name="password"

placeholder="Password"

className="border p-3 rounded w-full"

onChange={handleChange}

/>

<button

className="bg-green-600 text-white w-full py-3 rounded"

>

Register

</button>

</form>

<p className="text-center mt-4">

Already Registered?

<Link

to="/"

className="text-blue-600"

>

 Login

</Link>

</p>

</div>

</div>

);

}

export default Register;