import React from 'react'
import styles from './component.module.scss'
import Image from 'next/image'

const ChessSquare = ({ square }) => {
    let color;
    let img_url;
    if (square) {
        color = square._color === 'b' ? 'black': 'white'
        img_url = `/${color}_${square.name}.png`
    }
  return (
    <div className={styles.square}>
        {square &&     
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