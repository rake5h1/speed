const nodecallspython = require("node-calls-python");

const py = nodecallspython.interpreter;

py.import("./speed_test_01.py").then(function (pymodule) {
    const result = py.call(pymodule, "perform_speed_test");
    const res = Promise.resolve(result);
    res.then(function (res) { console.log(res) })
}).catch(e => console.log(e))