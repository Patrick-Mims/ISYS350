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
         for(i = 0; i < term.length; i++) {
             if(term[i].checked)
             {
                var t = term[i].value;
             }
         }

         var ir = (loan.value * (interestRate.value * 0.01)) / t;
         var p = ((loan.value / (t * 12)) + ir);

         /* test data */
         console.log("Interest Rate: ", (interestRate.value * 0.01));
         console.log("Loan: ", loan.value);
         console.log("Term: ", (t * 12));
         console.log("Ir: ", ir);
         console.log("P: ", p)

         if(discount.checked == true) { 
             payment.value = "$" + (p - (p * discount.value));
         } else {
             payment.value = "$" + p;
         }
     });
 })();
