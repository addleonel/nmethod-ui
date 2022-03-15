function getBisectionMethod(){
    var {PythonShell} = require('python-shell')
    var path = require('path')
    var thefunction = document.getElementById("thefunction").value
    var valor_a = document.getElementById("value_a").value
    var valor_b = document.getElementById("value_b").value
    var iterator = document.getElementById("iterator").value
    if ( iterator == ""){
        iterator = "0";
    }
    var options = {
        scriptPath: path.join(__dirname, '../engine/'),
        args: [thefunction, valor_a, valor_b, iterator]
    }

    var bisectionMethod = new PythonShell('bisection_method.py', options)
    bisectionMethod.on("message", function(message){
        swal("La iteración ",message);
    })
}