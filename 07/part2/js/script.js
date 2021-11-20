(function() {
     let loanAmount = document.getElementById("loanAmount");
     let submit = document.getElementById("submit");
     let monthlyPayment = document.getElementById("monthlyPayment");
     let interestRate = document.getElementById("interestRate");
     let vetDiscount = document.getElementById("discount");

     submit.addEventListener("click", function() {
         let result = (interestRate.value * loanAmount.value);

         if(discount.checked == true) { 
            let vetDiscount = (result * 0.5); 
            result = (result - vetDiscount);
         }

         monthlyPayment.value = result;
     });
 })();
