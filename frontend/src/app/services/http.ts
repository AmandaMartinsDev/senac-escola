import axios from "axios";

const client = axios.create({
  baseURL: "https://escola-backend.onrender.com/",
  // baseURL: "https://pokeapi.co/api/v2/",
  headers: { "Access-Control-Allow-Origin": "*" },
});

export default client;
