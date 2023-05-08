import axios from "axios";

const client = axios.create({
  baseURL: process.env.API_URL,
  timeout: 1000,
  headers: { "X-Custom-Header": "foobar" },
});

export default client;
