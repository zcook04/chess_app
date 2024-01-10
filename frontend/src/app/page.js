'use client'

import styles from './page.module.css'

export default function Home() {

  const handleClick = () => {

  }

  return (
    <main className={styles.main}>
      <div className={styles.button} onClick={e => handleClick(e)}>Start New Game</div>
    </main>
  )
}
