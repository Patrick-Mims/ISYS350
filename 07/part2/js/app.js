/* Author: Patrick Mims
 * Date: 11.18.21
 * Assignment: 7
 * Professor: David Chao
 * Purpose: this script simply calculates the monthly value 1347.13
 * */
(function() {
  var discount = document.getElementById("discount");
  var interestRate = document.getElementById("interestRate");
  var loan = document.getElementById("loanAmount");
  var payment = document.getElementById("monthlyPayment");
  var submit = document.getElementById("submit");
  var term = document.getElementsByName('term');

  submit.addEventListener("click", function() {
    var vetDiscount = 0.0;

    for(i = 0; i < term.length; i++) {
      if(term[i].checked)
      {
        var termInMonths = (term[i].value * 12);
      }
    }

    if(discount.checked == true) {
      vetDiscount = (50 * 0.01);
    }

    var convertedInterestRate = ((interestRate.value - vetDiscount) * 0.01);
    var monthlyPayment = (loan.value * (convertedInterestRate / 12) / (1 - (1 + (convertedInterestRate / 12))**-termInMonths));

    payment.value = "$" + monthlyPayment.toFixed(2);
  });
})();
