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

    const drawCheckeredBackground = (can, nRow, nCol) => {
        var ctx = can.getContext("2d");
        var w = can.width;
        var h = can.height;
    
        nRow = nRow || 8;    // default number of rows
        nCol = nCol || 8;    // default number of columns
    
        w /= nCol;            // width of a block
        h /= nRow;            // height of a block
    
        for (var i = 0; i < nRow; ++i) {
            for (var j = 0, col = nCol / 2; j < col; ++j) {
                ctx.rect(2 * j * w + (i % 2 ? 0 : w), i * h, w, h);
            }
        }
    
        ctx.fill();
    }

    return (
    <main className={styles.main}>
        <div className={styles.chessboard}>
            {board && board.map(row => row.map((square, idx) => <div className={styles.square}><ChessSquare key={idx} index={idx} square={square}/></div>))}
        </div>
    </main>
  )
}

export default page