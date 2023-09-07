@annotation
class MyClass {
  @property accessor bool = false
}

function annotation(...params) {
  console.log("------------ CLASS SECOND ------------")
  console.log(params)
}

function property(target, name) {
  console.log("------------ PROPERTY FIRST ------------")
  console.log(target, name)
  return {
    get() {
      console.log('get')
      return target.get.call(this)
    },
    set(val) {
      console.log('set', val)
      return target.set.call(this, val)
    }
  }
}

function debug(target, { kind, name }) {
  if (kind === 'accessor') {
    const { get, set } = target
    return {
      get() {
        console.log(`get ${name}`)
        return get.call(this)
      },
      set(val) {
        console.log(`set ${name} para ${val}`)
        return set.call(this, val)
      },
      init(initialValue) {
        console.log(`iniciando ${name} com o valor ${initialValue}`)
        return initialValue
      }
    }
  }
}

const a = new MyClass()
console.log(a.bool)
a.bool = true
console.log(a.bool)