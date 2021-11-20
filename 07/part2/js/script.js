/*
 * Author: Patrick Mims
 * Date: 11.18.21
 * Assignment: 7
 * Professor: David Chao
 * Purpose: this script simply calculates the monthly value
 * */

(function() {
     let interestRate = document.getElementById("interestRate"),
         loan = document.getElementById("loanAmount"),
         payment = document.getElementById("monthlyPayment"),
         submit = document.getElementById("submit"),
         vetDiscount = document.getElementById("discount");
     let term = document.getElementsByName('term');

         submit.addEventListener("click", function() {

             for(i = 0; i < term.length; i++) {
                 if(term[i].checked)
                 {
                    var t = term[i].value;
                 }
             }

             let total = t * (interestRate.value * loan.value);

             if(discount.checked == true) { 
                let vetDiscount = (total * 0.5); 
                total = (total - vetDiscount);
             }

             payment.value = "$" + total;
         });
 })();
