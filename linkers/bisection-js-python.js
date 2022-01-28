function getBisectionMethod(){
    var {PythonShell} = require('python-shell')
    var path = require('path')

    var valor_a = document.getElementById("value_a").value
    var valor_b = document.getElementById("value_b").value

    document.getElementById("value_a").value = ""
    document.getElementById("value_b").value = ""

    var output = "Intervalo: ["+valor_a+";"+valor_b+"]";
    document.getElementById("are").innerHTML = output;
    swal(output);

    var options = {
        scriptPath: path.join(__dirname, '../engine/'),
        args: [valor_a, valor_b]
    }

    var bisectionMethod = new PythonShell('bisection_method.py', options)

    bisectionMethod.on("message", function(message){
        swal("La iteración ", message)
    })
}