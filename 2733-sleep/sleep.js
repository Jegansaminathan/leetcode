/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    let myPromise= await new Promise((res,rej)=>{
        setTimeout(()=>{
            return res(millis)
        },millis)
    });
    return myPromise;
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */