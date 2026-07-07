import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import API from "../services/api";

function Login(){

    const navigate = useNavigate();

    const [form,setForm]=useState({

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

            const res=await API.post("/auth/login",form);

            localStorage.setItem("token",res.data.token);

            alert("Login Successful!");

            navigate("/dashboard");

        }

        catch(err){

            alert(err.response?.data?.detail || "Login Failed");

        }

    };

    return(

<div className="min-h-screen flex items-center justify-center">

<div className="bg-white shadow-xl rounded-xl p-8 w-[400px]">

<h1 className="text-3xl font-bold text-center mb-6">

SmartExpense AI

</h1>

<form onSubmit={handleSubmit} className="space-y-4">

<input

name="email"

placeholder="Email"

className="w-full border p-3 rounded"

onChange={handleChange}

/>

<input

type="password"

name="password"

placeholder="Password"

className="w-full border p-3 rounded"

onChange={handleChange}

/>

<button

className="w-full bg-blue-600 text-white py-3 rounded hover:bg-blue-700"

>

Login

</button>

</form>

<p className="mt-4 text-center">

Don't have an account?

<Link

to="/register"

className="text-blue-600"

>

 Register

</Link>

</p>

</div>

</div>

    );

}

export default Login;