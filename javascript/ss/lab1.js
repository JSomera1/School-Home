const input = [
    "buy",
    "it",
    "use",
    "it",
    "break",
    "it",
    "fix",
    "it",
    "trash",
    "it",
    "change",
    "it",
    "mail",
    "upgrade",
    "it",
  ];

const sort = (input) => {
    const dict = {}
    for ( let i = 0; i < input.length; i++ ) {
        list = []
        if (! (dict[input[i]] in dict)) {
            for ( let j = 0; j < input.length; j++ ) {
                if ( input[i] === input[j] ) {
                    list.push(j)
                }
            }
            dict[input[i]] = list
        }
        
    }
    return dict
    //then sort is somehow
}

console.log(sort(input))