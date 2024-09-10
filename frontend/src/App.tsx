import createClient from "openapi-fetch"
import { useEffect, useState } from "react"
import type { paths } from "./api-spec"

const api = createClient<paths>()

function App() {
  const [count, setCount] = useState<number>()

  useEffect(() => {
    async function fetch() {
      const { data, error } = await api.GET("/api/counter/count")
      if (error) {
        console.error(error)
        throw new Error("error occurred")
      }
      setCount(data.count)
    }
    fetch()
  }, [])

  async function increment() {
    const { data, error } = await api.POST("/api/counter/increment")
    if (error) {
      console.error(error)
      throw new Error("error occurred")
    }
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
