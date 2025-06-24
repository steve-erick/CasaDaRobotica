/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'robotic-blue': '#3ca2a2',
        'dark-robotic-blue': '#3674B5',
        'robotic-green': '#00FF9C',
        'robotic-dark': '#2d2d29',
        'robotic-white': '#dfece6',
      },
    },
  },
  plugins: [],
}