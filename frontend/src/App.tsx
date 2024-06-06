import { useState } from "react"

function App() {
  const [count, setCount] = useState<number>()

  // useEffect(() => {}, [])

  if (count === undefined) return <p>loading...</p>

  return <p>Count: {count}</p>
}

export default App
