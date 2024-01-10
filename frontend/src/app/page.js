'use client'

import styles from './page.module.scss'
import { useRouter } from 'next/navigation'

export default function Home() {
  const router = useRouter()

  const handleClick = () => {
   router.push('/play') 
  }

  return (
    <main className={styles.main}>
      <div className={styles.button} onClick={e => handleClick(e)}>Start New Game</div>
    </main>
  )
}
