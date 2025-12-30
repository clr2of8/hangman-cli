# Hangman Game in PowerShell (No ASCII Art)

$words = @("python", "hangman", "challenge", "programming", "openai", "computer", "science")

function Get-RandomWord {
    param($wordList)
    return $wordList | Get-Random
}

function Display-Board {
    param($missedLetters, $correctLetters, $secretWord, $maxGuesses)
    $guessesLeft = $maxGuesses - $missedLetters.Count
    Write-Host "Missed letters: $($missedLetters -join ' ')"
    Write-Host "Guesses left: $guessesLeft"
    $blanks = ($secretWord.ToCharArray() | ForEach-Object { if ($correctLetters -contains $_) { $_ } else { '_' } }) -join ' '
    Write-Host "Word: $blanks"
}

function Get-Guess {
    param($alreadyGuessed)
    while ($true) {
        $guess = Read-Host "Guess a letter"
        if ($guess.Length -ne 1) {
            Write-Host "Please enter a single letter."
        } elseif (-not ($guess -match '^[a-zA-Z]$')) {
            Write-Host "Please enter a LETTER."
        } elseif ($alreadyGuessed -contains $guess.ToLower()) {
            Write-Host "You have already guessed that letter. Choose again."
        } else {
            return $guess.ToLower()
        }
    }
}

function Play-Again {
    $response = Read-Host "Do you want to play again? (yes or no)"
    return $response.ToLower().StartsWith('y')
}

function Start-Hangman {
    $maxGuesses = 6
    Write-Host "HANGMAN GAME (PowerShell Edition)"
    do {
        $missedLetters = @()
        $correctLetters = @()
        $secretWord = Get-RandomWord $words
        $gameIsDone = $false
        while (-not $gameIsDone) {
            Display-Board $missedLetters $correctLetters $secretWord $maxGuesses
            $guess = Get-Guess ($missedLetters + $correctLetters)
            if ($secretWord.Contains($guess)) {
                $correctLetters += $guess
                if (($secretWord.ToCharArray() | Where-Object { $correctLetters -notcontains $_ }).Count -eq 0) {
                    Write-Host "Yes! The secret word is '$secretWord'! You have won!"
                    $gameIsDone = $true
                }
            } else {
                $missedLetters += $guess
                if ($missedLetters.Count -ge $maxGuesses) {
                    Display-Board $missedLetters $correctLetters $secretWord $maxGuesses
                    Write-Host "You have run out of guesses! The word was '$secretWord'."
                    $gameIsDone = $true
                }
            }
        }
    } while (Play-Again)
}

Start-Hangman
