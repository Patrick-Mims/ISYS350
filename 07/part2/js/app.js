/* Author: Patrick Mims
 * Date: 11.18.21
 * Assignment: 7
 * Professor: David Chao
 * Purpose: Simple Mortgage Calculator
 * */
(function() {
  var button = document.getElementById("submit");
  var discount = document.getElementById("discount");
  var loan = document.getElementById("loanAmount");
  var payment = document.getElementById("monthlyPayment");
  var rate = document.getElementById("interestRate");
  var term = document.getElementsByName('term');

  button.addEventListener("click", function() {
    var vetDiscount = 0.0, termInMonths = 120;

    /* Calculate Term */
    for(i = 0; i < term.length; i++) {
      if(term[i].checked) {
        termInMonths = (term[i].value * 12);
      }
    }

    /* Discount? */
    if(discount.checked == true) {
      vetDiscount = (50 * 0.01);
    }

    /* Calculate Monthly Payment */
    const convertedInterestRate = ((rate.value - vetDiscount) * 0.01);
    const monthlyPayment = (loan.value * (convertedInterestRate / 12) / (1 - (1 + (convertedInterestRate / 12))**-termInMonths));

    /* Output */
    payment.value = "$" + monthlyPayment.toFixed(2);
  });
})();
