// Given a function fn, return a new function that is identical to the original function except that it ensures fn is called at most once.

// The first time the returned function is called, it should return the same result as fn.
// Every subsequent time it is called, it should return undefined.

var once = function(fn) {
    var calls = 0
    return function(...args){
        if (calls === 0){
            calls += 1
            return fn(...args)
        }
    }
};

onceFn1 = once((a,b,c) => (a + b + c))
onceFn1([[1,2,3],[2,3,6]]) //6, undefined, fn was not called

onceFn2 = once((a,b,c) => (a * b * c))
onceFn2([[5,7,4],[2,3,6],[4,6,8]]) // 140, undefined, fn was not called, undefined, fn was not called

onceFn3 = once((a1,a2,a3,a4,a5,a6,a7) => (a1 * a5 - a7))
onceFn3([[6,4,2,4,5,3,2]]) // 28, undefined, fn was not called




