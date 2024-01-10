import React from 'react'
import styles from './component.module.scss'
import Image from 'next/image'

const ChessSquare = ({ square }) => {
    let color;
    let img_url;
    if (square.piece) {
        console.log(square.piece)
        color = square.piece._color === 'b' ? 'black': 'white'
        img_url = `/${color}_${square.piece.name}.png`
    }
  return (
    <div className={styles.square}>
        {square.piece &&     
        <Image
            src={img_url}
            width={75}
            height={75}
            alt={square.name}
        />}
    </div>
  )
}

export default ChessSquare