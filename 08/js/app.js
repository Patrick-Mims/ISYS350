/* Author: Patrick Mims
 * Date: 11.18.21
 * Assignment: 7
 * Professor: David Chao
 * Purpose: Simple Mortgage Calculator
 * Version: 2.0
 * */
(function() {
  var affordable = document.getElementById("affordablePayment");
  var button = document.getElementById("submit");
  var discount = document.getElementById("discount");
  var loan = document.getElementById("loanAmount");
  var payment = document.getElementById("monthlyPayment");
  var rate = document.getElementById("interestRate");
  var term = document.getElementsByName('term');

  button.addEventListener("click", function() {
    let mp = 0.0, termInMonths = 120, vetDiscount = 0.0;

    /* Calculate Term */
    for(i = 0; i < term.length; i++) {
      if(term[i].checked) {
        termInMonths = (term[i].value * 12);
      }
    }

    interest = (rate.value/100/12);

    /* Discount */
    if(discount.checked == true) {
      vetDiscount = (50 * 0.01);
    }

    /* Calculate Monthly Payment with Interest */
    interest = (((rate.value - vetDiscount))/100/12);

    mp = (loan.value * interest * (Math.pow(1 + interest, termInMonths)) / (Math.pow(1 + interest, termInMonths) - 1));

    /* Check if it's greater than or less than */
    (mp >= affordable.value) ? payment.style.backgroundColor = "#c00000" : payment.style.backgroundColor = "#006400";

    /* Output */
    payment.value = "$" + mp.toFixed(2);
  });
})();
