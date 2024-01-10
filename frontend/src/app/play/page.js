'use client'
import React, { useEffect, useState } from 'react'
import styles from './page.module.scss'

import ChessSquare from '@/components/ChessSquare/ChessSquare'

const page = () => {
    const [board, setBoard] = useState(null)

    useEffect(() => {
        fetch("http://localhost:8000/api/v1/game/newgame")
            .then(response => response.json())
            .then(data => setBoard(data.game?.board))
            .catch(error => console.error(error))
      },[])

    return (
    <main className={styles.main}>
        <div className={styles.chessboard}>
            {board && board.map((row, i) => row.map((square, j) => <div className={styles.square} key={i+j}><ChessSquare key={i+j} square={square}/></div>))}
        </div>
    </main>
  )
}

export default page