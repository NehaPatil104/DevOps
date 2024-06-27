function isPalindrome(str) {
  str = str.replace(/[\W_]/g, "").toLowerCase();
  let start = 0;
  let end = str.length - 1;

  while (start < end) {
    if (str[start++] != str[end--]) {
      return false;
    }
  }
  return true;
}

document.getElementById("check-btn").addEventListener("click", function () {
  let data = document.getElementById("text-input").value;

  if (data === "" || data === null) {
    alert("Please input a value");
  } else if (isPalindrome(data)) {
    document.getElementById("result").innerHTML = `${data} is a palindrome`;
  } else {
    document.getElementById("result").innerHTML = `${data} is not a palindrome`;
  }
});
