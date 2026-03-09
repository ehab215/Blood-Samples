/** @type {import('tailwindcss').Config} */
// eslint-disable-next-line import/no-anonymous-default-export
export default {
	content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
	theme: {
		extend: {
			colors: {
				primary: {
					100: "#f3e1f4",
					200: "#ddb5e5",
					300: "#c687d5",
					400: "#b066c9",
					500: "#884896",
					600: "#76418a",
					700: "#64397d",
					800: "#54316f",
					900: "#432861",
				},
			},
		},
	},
	plugins: [],
};
