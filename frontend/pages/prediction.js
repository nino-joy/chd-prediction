import { useState } from "react";

import Input from "../components/input";

function Prediction() {
	const [name, setName] = useState("");
	const [sex, setSex] = useState(1);
	const [age, setAge] = useState("");
	const [BP, setBP] = useState("");
	const [chol, setChol] = useState("");
	const [hdlChol, setHdlChol] = useState("");
	const [wCirc, setWCirc] = useState("");
	const [BMI, setBMI] = useState("");
	const [nFat, setNFat] = useState("");
	const [diabetic, setDiabetic] = useState(0);

	const [predVal, setPredVal] = useState();
	const [frsVal, setFrsVal] = useState();

	async function handleSubmit(e) {
		e.preventDefault();
		const data = {
			name: name,
			sex: sex,
			age: age,
			BP: BP,
			chol: chol,
			hdlChol: hdlChol,
			diabetic: diabetic,
			wCirc: wCirc,
			BMI: BMI,
			nFat: nFat,
		};
		let res = await fetch("http://localhost:5000/api/", {
			method: "POST",
			headers: {
				"Content-type": "application/json",
			},
			body: JSON.stringify(data),
		});

		res = await res.json();
		console.log(res.pred);
		console.log(res.frs);
		setPredVal(res.pred);
		setFrsVal(res.frs);
	}

	return (
		<div className="flex justify-center items-center sm:h-full">
			{/* FORM COMPONENT */}
			<div className="flex px-5 sm:my-14 my-5 sm:py-5 bg-white rounded-lg sm:shadow-xl sm:max-w-xl sm:border">
				<form action="" method="POST" onSubmit={handleSubmit}>
					<p className="mb-5 font-bold text-gray-800 text-2xl">
						Please fill in the details
					</p>

					<p className="mb-3 mt-10 font-semibold text-gray-800 text-md">
						Personal Profile
					</p>
					<Input
						type="name"
						width="full"
						placeholder="Full Name"
						name="name"
						onChange={(e) => {
							setName(e.target.value);
						}}
					/>

					<p className="mb-3 mt-10 font-semibold text-gray-800 text-md">
						Required Properties
					</p>

					{/* SELECT SEX */}
					<div className="mb-4">
						<label
							// for="sex"
							className="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400"
						>
							Sex
						</label>
						<select
							id="sex"
							className="border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
							// value={sex}
							onChange={(e) => {
								setSex(e.target.value === "Male" ? 1 : 2);
							}}
							required
						>
							<option>Male</option>
							<option>Female</option>
						</select>
					</div>

					<div className="flex sm:flex-row flex-col sm:space-x-10">
						<Input
							type="number"
							width="32"
							min="20"
							max="100"
							placeholder="Age"
							name="age"
							onChange={(e) => {
								setAge(e.target.value);
							}}
						/>

						<Input
							type="number"
							width="32"
							min="100"
							max="175"
							placeholder="SBP (mmHg)"
							onChange={(e) => {
								setBP(e.target.value);
							}}
						/>

						<Input
							type="number"
							width="32"
							min="100"
							max="400"
							placeholder="Cholestrol (mg/dL)"
							onChange={(e) => {
								setChol(e.target.value);
							}}
						/>
					</div>
					<Input
						type="number"
						width="full"
						min="10"
						max="100"
						placeholder="HDL Cholestrol (mg/dL)"
						onChange={(e) => {
							setHdlChol(e.target.value);
						}}
					/>

					<Input
						type="number"
						width="full"
						placeholder="Waist Circumference (cm)"
						onChange={(e) => {
							setWCirc(e.target.value);
						}}
					/>
					<Input
						type="number"
						width="full"
						min="5"
						max="70"
						placeholder="BMI"
						onChange={(e) => {
							setBMI(e.target.value);
						}}
					/>
					<Input
						type="number"
						width="full"
						placeholder="Neutral Fat (mg/dL)"
						onChange={(e) => {
							setNFat(e.target.value);
						}}
					/>

					<div className="mb-6">
						<label
							// for="countries"
							className="block mb-2 text-sm font-medium text-gray-900 dark:text-gray-400"
						>
							Diabetic
						</label>
						<select
							id="countries"
							className="border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-red-600 focus:border-red-600 block w-full p-2.5"
							// value={diabetic}
							onChange={(e) => {
								setDiabetic(e.target.value === "Yes" ? 1 : 0);
							}}
							required
						>
							<option>No</option>
							<option>Yes</option>
						</select>
					</div>
					<button
						type="submit"
						className="text-white bg-blue-600 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center"
					>
						Submit
					</button>
				</form>
			</div>

			{/* RESULT COMPONENT */}
			{predVal != null ? (
				<div
					className={`flex flex-col ml-28 p-4 max-w-sm h-full rounded-lg border-4 border-gray-200 shadow-md ${
						parseFloat(predVal * 100).toFixed(2) <= 50
							? "border-green-500"
							: parseFloat(predVal * 100).toFixed(2) > 50 &&
							  parseFloat(predVal * 100).toFixed(2) <= 75
							? "border-orange-400"
							: "border-red-600"
					}`}
				>
					<p className="text-gray-700 dark:text-gray-400">Your risk is at</p>
					<h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900">
						{parseFloat(predVal * 100).toFixed(2)} %
					</h5>

					{parseFloat(predVal * 100).toFixed(2) <= 50 ? (
						<p className="font-normal text-gray-700 dark:text-gray-400">
							Normal Condition
						</p>
					) : parseFloat(predVal * 100).toFixed(2) > 50 &&
					  parseFloat(predVal * 100).toFixed(2) <= 75 ? (
						<p className="font-normal text-gray-700 dark:text-gray-400">
							Slight Risk Condition
						</p>
					) : (
						<p className="font-normal text-gray-700 dark:text-gray-400">
							High Risk Condition
						</p>
					)}

					<h5 className="mt-5 text-xl font-bold tracking-tight text-gray-900">
						Framingham Risk Score (FRS): {frsVal}
					</h5>
				</div>
			) : (
				<div className="flex flex-col ml-28 p-4 max-w-sm h-full rounded-lg border border-gray-200 shadow-md">
					<h5 className="mb-2 text-2xl font-bold tracking-tight text-gray-900">
						Enter values to predict your risk
					</h5>
				</div>
			)}
		</div>
	);
}

export default Prediction;
