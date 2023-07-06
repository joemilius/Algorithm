// Write a function argumentsLength that returns the count of arguments passed to it.

var argumentsLength = function(...args) {
    console.log(args.length)
    return args.length
 
};

argumentsLength([5]) // 1
argumentsLength([{},null,"3"]) // 3