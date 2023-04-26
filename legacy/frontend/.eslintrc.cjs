module.exports = {
  parser: "@typescript-eslint/parser",
  parserOptions: {
    ecmaVersion: "latest",
    sourceType: "module",
    ecmaFeatures: {
      jsx: true,
    },
  },
  env: {
    node: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:@typescript-eslint:recommended",
    "plugin:vue/vue3-recommended",
    "plugin:prettier",
    "plugin:prettier/vue",
  ],
  rules: {},
};
