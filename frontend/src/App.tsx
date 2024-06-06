import { Fetcher } from "openapi-typescript-fetch"
import { useEffect, useState } from "react"
import type { paths } from "./api-spec"

const fetcher = Fetcher.for<paths>()

const getCounterCount = fetcher
  .path("/api/counter/count")
  .method("get")
  .create()

const postCounterIncrement = fetcher
  .path("/api/counter/increment")
  .method("post")
  .create()

function App() {
  const [count, setCount] = useState<number>()

  useEffect(() => {
    async function fetch() {
      const { data } = await getCounterCount({})
      setCount(data.count)
    }
    fetch()
  }, [])

  async function increment() {
    const { data } = await postCounterIncrement({})
    setCount(data.count)
  }

  if (count === undefined) return <p>loading...</p>

  return (
    <>
      <p>Count: {count}</p>
      <button type="button" onClick={increment}>
        ++
      </button>
    </>
  )
}

export default App
