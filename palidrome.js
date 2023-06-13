function isPalidrome(a)
{
    if (typeof a !== 'number')
    {
        return '${a} is not a number!';
    }
    
    a=a.toString().split('');

    for (var i=0; i<(a.length/2);i++)
    {
        if (a[1] !== a[a.length-1-i])
        {
            return false;
        }
    }
    return true;
}
//console.log(isPalidrome(121))

function largestPalidrome(){
    let ans=0

    for (let x=999; x>=100; x--){
        for (let y=999; y>=100;y--){
            let z=x*y;
            if (z<ans) break;
            if(isPalidrome(z) && z>ans){
                ans=z
            }
        }
    }
    return ans;
}
