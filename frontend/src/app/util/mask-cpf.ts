export const maskCpf = (cpf: string) => {
  if (cpf.length !== 11) {
    return cpf;
  }

  const cpfPart1 = cpf.slice(0, 3);
  const cpfPart2 = cpf.slice(3, 6);
  const cpfPart3 = cpf.slice(6, 9);
  const cpfPart4 = cpf.slice(9);

  return `${cpfPart1}.${cpfPart2}.${cpfPart3}-${cpfPart4}`;
};
