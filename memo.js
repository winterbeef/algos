// Memoization
var fibonacci = (function() {    // IIFE
    var memo = {};               // NOT visible outside the IIFE

    // Internal function;
    // Return fib(n), uses memo{} above.
    function f(n) {
        var value;
        // (1) Cache hit
        if (n in memo) {
            value = memo[n];
        // (2) Cache miss
        } else {
            // (a) Axiomatic cases
            if (n === 0 || n === 1)
                value = n;
            // (b) Hard work; recursive call
            else
                value = f(n - 1) + f(n - 2);
            // Store the value.
            memo[n] = value;
        }
        return value;
    }
    return f;
})();



function showHelp(help) {
  document.getElementById('help').innerHTML = help;
}

function setupHelp() {
  var helpText = [
      {'id': 'email', 'help': 'Your e-mail address'},
      {'id': 'name', 'help': 'Your full name'},
      {'id': 'age', 'help': 'Your age (you must be over 16)'}
    ];

  for (var i = 0; i < helpText.length; i++) {
    let item = helpText[i];  ///  VAR does NOT do what you expect!!! LET DOES.
    document.getElementById(item.id).onfocus = function() {
      showHelp(item.help);
    }
  }
}

setupHelp();