const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

readline.question('', (input) => {
  const [A, B] = input.split(' ').map(Number);
  console.log(A + B);
  readline.close();
});
