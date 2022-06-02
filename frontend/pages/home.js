import { Fragment } from "react";
import { Popover, Transition } from "@headlessui/react";
import { MenuIcon, XIcon } from "@heroicons/react/outline";
import Image from "next/image";

import landingIMG from "../assets/images/landing.jpeg";
import heartLOGO from "../assets/images/heartlogo.gif";

const navigation = [
	{ name: "About the Devs", href: "#" },
	{ name: "Learn More", href: "#" },
];

export default function Home() {
	return (
		<div className="h-screen bg-white overflow-hidden">
			<div className="max-w-7xl mx-auto">
				<div className="relative z-10 pb-8 bg-white sm:pb-16 md:pb-20 lg:max-w-2xl lg:w-full lg:pb-28 xl:pb-32 min-h-[50vh]">
					<svg
						className="hidden lg:block absolute right-0 inset-y-0 h-screen w-48 text-white transform translate-x-1/2"
						fill="currentColor"
						viewBox="0 0 100 100"
						preserveAspectRatio="none"
						aria-hidden="true"
					>
						<polygon points="50,0 100,0 50,100 0,100" />
					</svg>

					<Popover>
						<div className="sm:relative lg:fixed pt-6 px-4 sm:px-6 lg:px-8">
							<nav
								className="relative flex items-center justify-between sm:h-10 lg:justify-start"
								aria-label="Global"
							>
								<div className="flex items-center flex-grow flex-shrink-0 lg:flex-grow-0">
									<div className="flex items-center justify-between w-full md:w-auto">
										<a href="#">
											<span className="sr-only">Workflow</span>
											<Image
												// className="w-2 h-2"
												src={heartLOGO}
												height={40}
												width={40}
											/>
										</a>
										<div className="-mr-2 flex items-center md:hidden">
											<Popover.Button className="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
												<span className="sr-only">Open main menu</span>
												<MenuIcon className="h-6 w-6" aria-hidden="true" />
											</Popover.Button>
										</div>
									</div>
								</div>
								<div className="hidden md:block md:ml-10 md:pr-4 md:space-x-8">
									{navigation.map((item) => (
										<a
											key={item.name}
											href={item.href}
											className="font-medium text-gray-500 hover:text-gray-900"
										>
											{item.name}
										</a>
									))}
								</div>
							</nav>
						</div>

						<Transition
							as={Fragment}
							enter="duration-150 ease-out"
							enterFrom="opacity-0 scale-95"
							enterTo="opacity-100 scale-100"
							leave="duration-100 ease-in"
							leaveFrom="opacity-100 scale-100"
							leaveTo="opacity-0 scale-95"
						>
							<Popover.Panel
								focus
								className="absolute z-10 top-0 inset-x-0 p-2 transition transform origin-top-right md:hidden"
							>
								<div className="rounded-lg shadow-md bg-white ring-1 ring-black ring-opacity-5 overflow-hidden">
									<div className="px-5 pt-4 flex items-center justify-between">
										<div className="-mr-2">
											<Popover.Button className="bg-white rounded-md p-2 inline-flex items-center justify-center text-gray-400 hover:text-gray-500 hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-inset focus:ring-indigo-500">
												<span className="sr-only">Close main menu</span>
												<XIcon className="h-6 w-6" aria-hidden="true" />
											</Popover.Button>
										</div>
									</div>
									<div className="px-2 pt-2 pb-3 space-y-1">
										{navigation.map((item) => (
											<a
												key={item.name}
												href={item.href}
												className="block px-3 py-2 rounded-md text-base font-medium text-gray-700 hover:text-gray-900 hover:bg-gray-50"
											>
												{item.name}
											</a>
										))}
									</div>
								</div>
							</Popover.Panel>
						</Transition>
					</Popover>

					<div className=" lg:flex lg:h-screen md:pt-10 lg:pt-0 px-10 min-h-[50vh] flex">
						<div className="flex justify-center items-center">
							<div className="sm:text-center lg:text-left lg:mr-8">
								<h1 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
									<span className="block xl:inline">Optimal DNN Based</span>{" "}
									<span className="block text-red-600 xl:inline">
										Coronary Heart Disease Prediction
									</span>
								</h1>
								<p className="mt-3 text-base text-gray-500 sm:mt-5 sm:text-lg sm:max-w-xl sm:mx-auto md:mt-5 md:text-xl lg:mx-0">
									Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure
									qui lorem cupidatat commodo. Elit sunt amet fugiat veniam
									occaecat fugiat aliqua.
								</p>
								<div className="mt-5 sm:mt-8 sm:flex sm:justify-center lg:justify-start">
									<div className="rounded-md shadow">
										<a
											href="/prediction"
											className="w-full flex items-center justify-center px-8 py-3 border border-transparent text-base font-medium rounded-md text-white bg-red-600 hover:bg-red-700 md:py-4 md:text-lg md:px-10"
										>
											Get started
										</a>
									</div>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
			<div className="lg:absolute lg:inset-y-0 lg:right-0 lg:w-1/2">
				<Image
					className="w-full object-cover sm:h-72 md:h-96 lg:w-full h-full"
					src={landingIMG}
					alt="Pic of heart"
					layout="fill"
				/>
			</div>
		</div>
	);
}
