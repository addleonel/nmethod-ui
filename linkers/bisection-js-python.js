

function getBisectionMethod(){
    var theFunction = document.getElementById("thefunction").value
    var valorA = document.getElementById("value_a").value
    var valorB = document.getElementById("value_b").value
    var iterator = document.getElementById("iterator").value
    if ( iterator == ""){
        iterator = "0";
    }

    var result = bisectionMethod(
        theFunction, 
        Number.parseFloat(valorA), 
        Number.parseFloat(valorB), 
        Number.parseInt(iterator)
    );
    console.log(result)
    swal("La iteración ", );
}