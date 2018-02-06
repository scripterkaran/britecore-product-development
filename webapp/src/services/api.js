
let RISK_MANAGEMENT_API = {
  base: function () {
    return 'risks/'
  },
  get : function (id) {
    return this.base() +  id  + '/'
  },
  list : function () {
    return this.base()
  }

}


export {RISK_MANAGEMENT_API}
