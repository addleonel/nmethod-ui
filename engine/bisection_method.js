const mathjs = require("mathjs");

var func_expresions, iterator, valor_a, valor_b;

function bisectionMethod(f, x_a, x_b, iterator) {
  /*
  x_a and x_b are intervals
  */
  var error, f_a, f_r, i, rows, sig, x_r, x_r_before;
  i = 1;
  x_r_before = 0;
  rows = [];

  while (true) {
    f_a = mathjs.evaluate(f, {
      "x": x_a,
    });
    x_r = (x_a + x_b) / 2;
    f_r = mathjs.evaluate(f, {
        "x": x_r,
    });

    rows.push({'i': i, 'x_a': x_a, 'x_b': x_b , 'x_r': x_r, 'f_r': f_r});
    console.log(i)
    if (i === iterator) {
        return rows;
    }

    error = Math.abs((x_r - x_r_before) / x_r) * 100;

    if (i > 500) {
        return rows;
    }

    sig = f_a * f_r;

    if (sig > 0) {
      x_a = x_r;
    } else {
      if (sig < 0) {
        x_b = x_r;
      }
    }

    x_r_before = x_r;
    i = i + 1;
  }
}

// func_expresions = "x^3-x-2";
// valor_a = 1;
// valor_b = 2;
// iterator = 15;
// console.log(bisectionMethod(func_expresions, valor_a, valor_b, iterator));
