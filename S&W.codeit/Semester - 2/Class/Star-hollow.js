n = 10;
for (i = 1; i <= n; i++) {
  space = " ".repeat(n - i);
  for (j = 1; j <= i; j++) {
    if (i === n) {
      console.log("*".repeat(n));
      break;
    }
  }
}
for (i = n - 1; i > 0; i--) {
  space = " ".repeat(n - i);
  for (j = 1; j <= i; j++) {
    if (i === n) {
      console.log("*".repeat(n));
      break;
    }
  }
}
